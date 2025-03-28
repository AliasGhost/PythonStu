from PIL import Image

def convert_png_to_bmp(input_path, output_path):
    try:
        # 打开PNG图片
        with Image.open(input_path) as img:
            # 处理RGBA或P模式（调色板透明）
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            # 保存为BMP格式
            img.save(output_path, 'BMP')
            print(f"成功将 {input_path} 转换为 {output_path}")
    except Exception as e:
        print(f"转换失败: {e}")

# 示例用法
if __main__ == __name__:
    convert_png_to_bmp('image_in.jpg', '1-Img2bmp/image_out.bmp')