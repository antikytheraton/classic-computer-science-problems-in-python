from secrets import token_bytes
from typing import Tuple, List


IMAGE_PATH: str = 'src/1.3/img.jpg'


class ImageEncrypt:
    def __init__(self, image_path: str) -> None:
        self.original_image = self._load_image(image_path)

    def _load_image(self, path: str) -> bytearray:
        with open(path, 'rb') as image:
            f = image.read()
            return bytearray(f)

    @property
    def fake_key(self):
        return self._random_key(len(self.original_image))

    def _write_image(self, path: str, byte_image: bytes):
        with open(path, '+wb') as f:
            f.write(byte_image)

    def _random_key(self, length: int) -> int:
        tb: bytes = token_bytes(length)
        return int.from_bytes(tb, "big")

    def encrypt(self) -> Tuple[int, int]:
        dummy: int = self._random_key(len(self.original_image))
        original_key: int = int.from_bytes(self.original_image, 'big')
        encrypted: int = original_key ^ dummy   # XOR
        return dummy, encrypted

    def decrypt(self, key1: int, key2:int) -> None:
        decrypted: int = key1 ^ key2    # XOR
        temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
        self._write_image('src/1.3/result.jpg', temp)


if __name__ == "__main__":
    image = ImageEncrypt(IMAGE_PATH)
    key1, key2 = image.encrypt()
    fake_key = image.fake_key
    image.decrypt(key1, key2)
