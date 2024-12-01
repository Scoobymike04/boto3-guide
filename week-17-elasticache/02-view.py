import boto3
import time

# Initialize the ElastiCache client
elasticache = boto3.client('elasticache')

# Specify the cluster ID
cluster_id = 'justjules-redis-cluster'  # Replace with the desired cluster ID

# Maximum number of retries
max_retries = 10
retry_count = 0
wait_time = 10  # seconds

while retry_count < max_retries:
    try:
        # Describe the Redis cluster
        response = elasticache.describe_cache_clusters(
            CacheClusterId=cluster_id,
            ShowCacheNodeInfo=True
        )
        
        # Display relevant cluster information
        if response['CacheClusters']:
            cluster_info = response['CacheClusters'][0]
            print("Cluster ID:", cluster_info['CacheClusterId'])
            print("Status:", cluster_info['CacheClusterStatus'])
            print("Node Type:", cluster_info['CacheNodeType'])
            print("Engine:", cluster_info['Engine'])
            
            # Check if the cluster is available and has CacheNodes information
            if cluster_info['CacheClusterStatus'] == 'available' and 'CacheNodes' in cluster_info:
                print("Endpoint Address:", cluster_info['CacheNodes'][0]['Endpoint']['Address'])
                print("Port:", cluster_info['CacheNodes'][0]['Endpoint']['Port'])
            else:
                print("Cluster is not yet fully available. Cache nodes are not accessible.")
            break
    except elasticache.exceptions.CacheClusterNotFoundFault:
        print("Cluster not found. Retrying...")
        retry_count += 1
        time.sleep(wait_time)
else:
    print("Max retries reached. Cluster may not be available yet.")
