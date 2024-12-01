import boto3

# Initialize the ElastiCache client
elasticache = boto3.client('elasticache')

# Configuration for the Redis cluster
cluster_id = 'justjules-redis-cluster'  # Replace with your preferred cluster ID
node_type = 'cache.t2.micro'     # Replace with the desired node type

# Create the Redis cluster
response = elasticache.create_cache_cluster(
    CacheClusterId=cluster_id,
    Engine='redis',
    CacheNodeType=node_type,
    NumCacheNodes=1
)

# Print the details of the created Redis cluster
print("Redis cluster created:", response['CacheCluster']['CacheClusterId'])