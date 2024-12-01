import boto3

# Initialize the ElastiCache client
elasticache = boto3.client('elasticache')

# Specify the cluster ID
cluster_id = 'justjules-redis-cluster'  # Replace with the desired cluster ID

# Delete the Redis cluster
response = elasticache.delete_cache_cluster(CacheClusterId=cluster_id)
print(f"Redis cluster '{cluster_id}' deletion initiated.")