from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Document
import pymupdf4llm
import os
from django.conf import settings
from django.core.files.base import ContentFile

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    document_list = Document.objects.filter(user=request.user).order_by('-uploaded_at')
    
    # Pagination - 10 items per page
    paginator = Paginator(document_list, 10)
    page_number = request.GET.get('page')
    documents = paginator.get_page(page_number)
    
    return render(request, 'dashboard.html', {'documents': documents})

@login_required
def upload_view(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('pdf_file')
        title = request.POST.get('title', 'Untitled')
        
        if pdf_file:
            # Validate file type
            if not pdf_file.name.lower().endswith('.pdf'):
                return render(request, 'upload.html', {'error': 'Only PDF files are allowed.'})
            
            # Validate file size (50MB limit)
            if pdf_file.size > 50 * 1024 * 1024:
                return render(request, 'upload.html', {'error': 'File size must be under 50MB.'})
                
            # Save document first to get the PDF path
            document = Document.objects.create(
                user=request.user,
                title=title,
                pdf_file=pdf_file
            )
            
            # Use pymupdf4llm to convert
            pdf_path = document.pdf_file.path
            
            try:
                import re
                md_text = pymupdf4llm.to_markdown(pdf_path)
                
                # Remove pymupdf4llm's default 'picture intentionally omitted' messages
                md_text = re.sub(r'==>\s*picture.*?intentionally\s*omitted\s*<==\n?', '', md_text)
                
                # Create markdown file name
                base_name = os.path.splitext(os.path.basename(pdf_path))[0]
                md_filename = f"{base_name}.md"
                
                # Save markdown text to file field
                document.markdown_file.save(md_filename, ContentFile(md_text.encode('utf-8')))
                document.save()
                
                return redirect('preview', doc_id=document.id)
            except Exception as e:
                # Handle error
                document.delete()
                return render(request, 'upload.html', {'error': str(e)})
                
    return render(request, 'upload.html')

@login_required
def preview_view(request, doc_id):
    document = get_object_or_404(Document, id=doc_id, user=request.user)
    md_content = ""
    if document.markdown_file and os.path.exists(document.markdown_file.path):
        with open(document.markdown_file.path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
    return render(request, 'preview.html', {
        'document': document,
        'md_content': md_content
    })

@login_required
def delete_document_view(request, doc_id):
    document = get_object_or_404(Document, id=doc_id, user=request.user)
    if request.method == 'POST':
        document.delete()
        return redirect('dashboard')
    return redirect('dashboard')

@login_required
def bulk_delete_documents_view(request):
    if request.method == 'POST':
        document_ids = request.POST.getlist('document_ids')
        if document_ids:
            # We must iterate and call delete() on each instance 
            # to trigger the custom model delete() which cleans up files.
            docs_to_delete = Document.objects.filter(id__in=document_ids, user=request.user)
            for doc in docs_to_delete:
                doc.delete()
    return redirect('dashboard')
