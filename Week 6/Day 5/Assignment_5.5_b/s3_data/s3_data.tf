resource "aws_s3_bucket" "s3_data" {
    bucket = var.bucket_name
}
resource "aws_s3_bucket_acl" "s3_data_acl" {
  bucket = aws_s3_bucket.s3_data.id
  acl    = var.acl_value
}
resource "aws_s3_object" "folder" {
    bucket = "${aws_s3_bucket.s3_data.id}"
    key    = "day2/IaC/"
    acl    = var.acl_value
    source = "/dev/null"
}