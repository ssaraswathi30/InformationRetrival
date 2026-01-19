#!/usr/bin/env python3
"""Script to generate PDF paper files for the data folder"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from pathlib import Path

# Create data directory if it doesn't exist
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

# Sample papers data for PDF generation
pdf_papers = [
    {
        "id": 1,
        "title": "Deep Learning for Computer Vision: A Survey",
        "abstract": "This paper provides a comprehensive survey of deep learning techniques applied to computer vision tasks. We examine convolutional neural networks, recurrent architectures, and transformer-based models for image classification, object detection, and semantic segmentation. State-of-the-art performance metrics are discussed across multiple benchmark datasets."
    },
    {
        "id": 5,
        "title": "Recurrent Neural Networks for Sequence Modeling",
        "abstract": "Recurrent neural networks handle sequential data by maintaining hidden state across time steps. This paper examines long short-term memory networks, gated recurrent units, and bidirectional RNNs. Applications span time series forecasting, language modeling, and video analysis."
    },
    {
        "id": 10,
        "title": "Meta-Learning: Learning to Learn",
        "abstract": "Meta-learning enables models to quickly adapt to new tasks with minimal data. This paper examines model-agnostic meta-learning, prototypical networks, and siamese networks. Few-shot learning and zero-shot learning paradigms are thoroughly analyzed."
    },
    {
        "id": 15,
        "title": "Object Detection: YOLO, Faster R-CNN, and SSD",
        "abstract": "Object detection is fundamental for computer vision applications. This paper compares single-stage detectors (YOLO, SSD) and two-stage detectors (Faster R-CNN, Mask R-CNN). Performance benchmarks and architectural innovations are thoroughly reviewed."
    },
    {
        "id": 20,
        "title": "Named Entity Recognition: Techniques and Applications",
        "abstract": "Named entity recognition identifies and classifies entities in text. This paper reviews CRF-based approaches, RNN-based models, and transformer-based NER systems. Biomedical NER and cross-lingual NER are explored."
    }
]

# Define custom styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=14,
    textColor='#1a1a1a',
    spaceAfter=12,
)
abstract_style = ParagraphStyle(
    'CustomAbstract',
    parent=styles['Normal'],
    fontSize=11,
    textColor='#333333',
    spaceAfter=12,
    leading=14,
)

# Create PDF files
for paper in pdf_papers:
    pdf_path = data_dir / f"paper_{paper['id']}.pdf"
    doc = SimpleDocTemplate(str(pdf_path), pagesize=letter)
    story = []
    
    # Add title
    story.append(Paragraph(paper['title'], title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Add abstract content
    story.append(Paragraph(paper['abstract'], abstract_style))
    
    # Build the PDF
    doc.build(story)
    print(f"Created: {pdf_path}")

print(f"\nSuccessfully created {len(pdf_papers)} PDF paper files in the data folder!")
