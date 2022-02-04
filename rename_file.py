import os

user_id_arr = ["the_test_01", "the_test_02", "the_test_03", "the_test_04", "the_test_05", "the_test_06"]
# user_id_arr = ["the_test_05"]
query = \
    f"INSERT INTO i_upload_img_data(user_id, fileDir, filename, status, regdate) \n" \
    f"VALUES \n"
for user_id in user_id_arr:
    file_path = f"D:\\ZHKim\\programs\\aitom\\public_html_ai\\data\\image\\extract_face\\{user_id}"
    file_names = os.listdir(file_path)

    i = 1
    for name in file_names:
        arr = name.split('.')
        ext = arr[len(arr)-1]
        filename = f"f{i}.{ext}"
        query += f"('{user_id}', 'data/image/extract_face/{user_id}', '{filename}', 'upload', NOW()),\n"
        try:
            src = os.path.join(file_path, name)
            dst = os.path.join(file_path, filename)
            os.rename(src, dst)
        except:
            pass
        i += 1


# file_names = os.listdir(file_path)
# for name in file_names:
#     query += f"('{user_id}', 'data/image/extract_face/{user_id}', '{name}', 'upload', NOW()),\n"
# print(file_names)

print(query)

