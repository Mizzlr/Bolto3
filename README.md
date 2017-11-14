# Bolto3

Like [Boltons](https://github.com/mahmoud/boltons) for [Boto3](https://github.com/boto/boto3).

### Installation

```sh
$ pip install bolto3
```

### Features added in v1.0:

* `bolto3.s3utils.S3UrlParser` - Converts "Bucket/Key" into S3 URL and vice versa.
* `bolto3.ec2utils.Ec2IpPortFinder` - Finds host IP and Port given an ECS service name.
* `bolto3.ecsutils.EcsServiceKiller` - Kills ECS services given an ECS service name.

```py
>>> from bolto3.s3utils import S3UrlParser
>>> parser = S3UrlParser()
>>> parser.parse_s3_url('s3://bucket/prefix/key.txt')
S3UrlParseResult(scheme="s3", region="", bucket="bucket", key="prefix/key.txt")
```
