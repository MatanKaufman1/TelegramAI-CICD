from setuptools import setup, find_packages

pyTelegramBotAPI_setup_args = dict(
    name='pyTelegramBotAPI',
    version='4.12.0',
    description='pyTelegramBotAPI',
    license='GPL2',
    install_requires=[
        'yt-dlp>=2023.2.17',
        'pyTelegramBotAPI',
        'boto3',
        'loguru',
        'python>=3.5',
    ],
    author='Matt',
    author_email='example@example.com'
)

if __name__ == '__main__':
    setup(**pyTelegramBotAPI_setup_args)


