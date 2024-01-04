from rembg import remove
from PIL import Image
from pathlib import Path


# https://github.com/danielgatis/rembg/blob/main/README.md

def remove_background():
    list_of_file = ['*.png', '*.jpg', '*jpeg']
    all_files = []

    for ex in list_of_file:
        all_files.extend(Path('C:/Users/user/PycharmProjects/githubyo/inputforremovebk').glob(ex))

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'C:/Users/user/PycharmProjects/githubyo/outputforremovebk/{file_name}_output.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        print(f'Completed: {index + 1} / {len(all_files)}')


def main():
    remove_background()


if __name__ == '__main__':
    main()
