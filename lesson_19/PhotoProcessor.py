import requests
import os


class PhotoProcessor:
    def __init__(self):
        self.counter = 1
        self.api_nasa_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=zILa7AxeyaiCKAeAvWs0DGgE6scYtqy033ceI1T8'
        self.file_name = None

    def save_from_nasa(self):
        response = requests.get(self.api_nasa_url)
        json_data = response.json()
        for value in json_data['photos']:
            photo_url = value['img_src']
            photo = requests.get(photo_url)
            with open(self.file_name_generator(), 'wb') as file:
                file.write(photo.content)
            self.counter += 1

    def file_name_generator(self):
        self.file_name = f'mars_photo_{self.counter}.jpg'
        return self.file_name

    def post_image(self, file_name=None):
        photos_names = []
        if file_name is None:
            self.save_from_nasa()
            photos_names = self.get_all_photos_names()
        else:
            photos_names = [file_name]
        for photo in photos_names:
            url = f"http://127.0.0.1:8080/upload"
            with open(photo, 'rb') as file:
                files = {'image': file}
                response = requests.post(url, files=files)
                if response.status_code != 201:
                    print(f"Error uploading {photo}: {response.text}")
                else:
                    print(f"Image POSTed: {response.json()}")

    @staticmethod
    def get_all_photos_names():
        photos_list = []
        files = os.listdir()
        for file in files:
            if file.endswith('.jpg'):
                photos_list.append(file)
        return photos_list

    @staticmethod
    def get_image(file_name: str, content_type='text'):
        headers = {'Content-Type': content_type}
        if file_name:
            url = f"http://127.0.0.1:8080/image/{file_name}"
            response = requests.get(url=url, headers=headers)
            if content_type == 'text':
                print(response.text)
            if content_type == 'image':
                with open('downloaded_img.jpg', 'wb') as file:
                    file.write(response.content)
                    print(f"Got image downloaded_img.jpg")

    @staticmethod
    def delete_image(file_name):
        url = f"http://127.0.0.1:8080/delete/{file_name}"
        response = requests.delete(url)
        if response.status_code != 200:
            print(f"Error deleting {file_name}: {response.text}")
        else:
            print(f"Image {file_name} deleted")


if __name__ == '__main__':
    pp = PhotoProcessor()
    pp.post_image()
    pp.get_image(file_name='mars_photo_2.jpg', content_type='image')
    pp.delete_image(file_name='mars_photo_2.jpg')


