import requests
from datetime import datetime

from .get_response import get_response


def get_content(unknown_link: str, telegram_id: int) -> dict | None:
    # Getting json from response
    try:
        data = get_response(unknown_link=unknown_link).json()
    except:
        data = None
    if not data:
        return None

    # file - object that contains all required information about content
    file = {
        'title': None if data['Type'] == 'Story-Video' else data['title'],
        'many': False
    }

    # Identifying a datatype of content -> Carousel, Post-Video, Post-Image
    if data['Type'] == 'Carousel':
        file_names = []
        for i, l in enumerate(data['media']):
            # Setting a file name
            file_name = f"media/posts/{telegram_id}-{str(datetime.now()).replace(' ', '_')}.jpeg"

            # Saving every image
            r = requests.get(l)
            with open(file_name, 'wb') as f:
                f.write(r.content)
                file_names.append(file_name)

        file['content'] = data['media']
        file['many'] = True
        file['file_name'] = file_names

    else:
        # Identifying an extension of a file: extension -> mp4, jpg, webp
        extension = data['media'].split("/")[-1].split("?")[0].split(".")[-1]

        if data['Type'] in ['Post-Video', 'Story-Video']:
            # Setting a file name
            file_name = f"media/video/{telegram_id}-{str(datetime.now()).replace(' ', '_')}.mp4"

            r = requests.get(data['media'], stream=True)
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)

            file['content'] = data['media']
            file['extension'] = extension
            file['file_name'] = file_name

        elif data['Type'] == 'Post-Image':
            # Setting a file name
            file_name = f"media/posts/{telegram_id}-{str(datetime.now()).replace(' ', '_')}.jpeg"

            r = requests.get(data['media'])
            with open(file_name, 'wb') as f:
                f.write(r.content)

            file['content'] = data['media']
            file['extension'] = extension
            file['file_name'] = file_name

    return file

# "<b>@{txt} tomonidan yuklandi</b>"