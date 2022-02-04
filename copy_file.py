import shutil

user_id_arr = ["the_test_01", "the_test_02", "the_test_03", "the_test_04", "the_test_05", "the_test_06"]
for user_id in user_id_arr:
    shutil.copytree("D:\\ZHKim\\programs\\tmp\\testimage\\test", f"D:\\ZHKim\\programs\\aitom\\public_html_ai\\data\\image\\extract_face\\{user_id}")