from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn.
    Sử dụng Pydantic để đảm bảo tính toàn vẹn dữ liệu.
    """
    document_id: str
    source_type: str  # Ví dụ: 'PDF' hoặc 'Video'
    author: str
    category: str
    content: str
    timestamp: str
