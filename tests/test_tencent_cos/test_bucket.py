import uuid
from unittest import TestCase, main

from src.tencent_cos.cos import TencentCos
from src.tencent_cos.cos_bucket import TencentCosBucket
from src.utils.file_tools import get_file_md5sum

# to run test, the following 2 params must be given
SECRET_ID = 'your_secret_id'
SECRET_KEY = 'your_secret_key'


class TestTencentCos(TestCase):
    def setUp(self) -> None:
        self.cos = TencentCos(SECRET_ID, SECRET_KEY)
        self.test_bucket_name = f'python-ut'
        if self.test_bucket_name in self.cos.list_buckets():
            self.bucket = TencentCosBucket(self.cos, self.test_bucket_name)
            self.bucket.delete_all_objects()
        else:
            self.cos.create_bucket(self.test_bucket_name)
            self.bucket = TencentCosBucket(self.cos, self.test_bucket_name)

    def tearDown(self) -> None:
        # delete all objects
        self.bucket.delete_all_objects()
        # delete bucket
        self.cos.delete_bucket(self.test_bucket_name)

    def test_mkdir(self):
        dir_name = 'test1'
        self.bucket.mkdir(dir_name)
        self.assertIn(dir_name, self.bucket.list_dirs())

    def test_list_files(self):
        bucket = TencentCosBucket(self.cos, 'obsidian')
        objects = bucket.list_objects()
        dirs = bucket.list_dirs()
        files = bucket.list_files()

    def test_ops_bucket(self):
        buckets_before = self.cos.list_buckets()
        new_bucket_name = f'python-ut-{uuid.uuid4().hex[:5]}'
        self.assertNotIn(new_bucket_name, buckets_before)

        self.cos.create_bucket(new_bucket_name)
        buckets_after_created = self.cos.list_buckets()
        self.assertIn(new_bucket_name, buckets_after_created)

        self.cos.delete_bucket(new_bucket_name)
        buckets_after_deleted = self.cos.list_buckets()
        self.assertNotIn(new_bucket_name, buckets_after_deleted)

    def test_check_file_md5(self):
        test_file = 'your_local_file'
        md5_local = get_file_md5sum(test_file)

        files_before_upload = self.bucket.list_objects()
        result, msg = self.bucket.upload_object(test_file)
        self.assertTrue(result)
        files_after_upload = self.bucket.list_objects()

        md5_remote = self.bucket.get_object_md5hash('your_remote_file')
        self.assertEqual(md5_remote, md5_local)


if __name__ == "__main__":
    main()
