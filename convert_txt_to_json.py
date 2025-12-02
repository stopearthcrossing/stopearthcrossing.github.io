import os
import json
import glob

def create_documents_json(txt_folder, output_file='Yi_documents.json'):
    """
    将TXT文件夹中的所有文件转换为一个JSON文件
    
    Args:
        txt_folder: 包含TXT文件的文件夹路径
        output_file: 输出的JSON文件名
    """
    documents = []
    
    # 获取所有TXT文件
    #txt_files = glob.glob(os.path.join(txt_folder, "*.txt"))
    txt_files = glob.glob(os.path.join(txt_folder, "i_*"))  # 根据文件夹内文件名调整了代码
    
    for i, file_path in enumerate(sorted(txt_files)):
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取文件名（不含扩展名）
        filename = os.path.basename(file_path)
        title = os.path.splitext(filename)[0]
        
        # 创建文档对象
        doc = {
            "id": filename.split("_")[1],
            "title": title,
            "filename": filename,
            "content": content
        }
        
        documents.append(doc)
    
    # 创建JSON结构
    data = {
        "documents": documents
    }
    
    # 写入JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"成功创建 {output_file}，包含 {len(documents)} 个文档")

# 使用示例
if __name__ == "__main__":
    create_documents_json("gua_ci")  # 替换为您的TXT文件夹路径