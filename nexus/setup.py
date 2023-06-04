from setuptools import setup, find_packages

pyTelegramBotAPI_setup_args = dict(
    name='pyTelegramBotAPI',
    version='1.0.0',
    description='pyTelegramBotAPI',
    license='MIT',
    install_requires=[
        'yt-dlp>=2023.2.17',
        'pyTelegramBotAPI',
        'boto3',
        'loguru',
    ],
    author='Matt',
    author_email='example@example.com'
)

if __name__ == '__main__':
    setup(**pyTelegramBotAPI_setup_args)


