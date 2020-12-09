from distutils.core import setup, Extension

def generateModule():
    setup(name="fputs",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="Mahanth Mohan",
          author_email="mohan.mahanth@gmail.com",
          ext_modules=[Extension("fputs", ["fputsModule.c"])]
        )

if __name__ == "__main__":
    generateModule()
