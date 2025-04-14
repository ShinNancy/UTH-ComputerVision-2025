import os
import glob
import subprocess

def open_excel_from_desktop(filename_contains=None):
    # Lấy đường dẫn Desktop hiện tại của người dùng
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Tìm tất cả file .xlsx trên desktop
    search_pattern = os.path.join(desktop_path, "*.xlsx")
    excel_files = glob.glob(search_pattern)

    # Nếu muốn tìm theo từ khoá trong tên file
    if filename_contains:
        excel_files = [f for f in excel_files if filename_contains.lower() in os.path.basename(f).lower()]

    if not excel_files:
        print("⚠️ Không tìm thấy file Excel nào trên Desktop.")
        return

    # Mở file đầu tiên tìm thấy
    file_to_open = excel_files[0]
    print(f"📂 Đang mở file: {file_to_open}")

    try:
        subprocess.Popen(['start', '', file_to_open], shell=True)
    except Exception as e:
        print(f"❌ Lỗi khi mở file Excel: {e}")
