from PhotoProcessor import PhotoProcessor


pp = PhotoProcessor()
pp.post_image('photo_for_uploading.jpg')
pp.get_image(file_name='photo_for_uploading.jpg', content_type='text')
pp.delete_image(file_name='photo_for_uploading.jpg')
