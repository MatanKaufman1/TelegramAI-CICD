from setuptools import setup, find_packages

loguru_setup_args = dict(
    name='loguru',
    version='0.7.0',
    description='loguru',
    license='MIT',
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
    setup(**loguru_setup_args)


