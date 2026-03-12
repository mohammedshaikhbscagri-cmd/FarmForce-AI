output "api_url" {
  description = "Backend API URL"
  value       = "http://${aws_instance.backend.public_ip}:8000"
}

output "db_endpoint" {
  description = "RDS PostgreSQL endpoint"
  value       = aws_db_instance.postgres.endpoint
}

output "redis_endpoint" {
  description = "ElastiCache Redis endpoint"
  value       = aws_elasticache_cluster.redis.cache_nodes[0].address
}

output "s3_bucket_name" {
  description = "S3 media bucket name"
  value       = aws_s3_bucket.media.bucket
}
