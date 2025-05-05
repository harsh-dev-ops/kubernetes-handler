from kubernetes import client, config

class KubernetesHandlerReference:
    def __init__(self):
        # Load kubeconfig from default location
        config.load_kube_config()
        
        # Initialize API clients
        self.core_v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()
        self.batch_v1 = client.BatchV1Api()
    
    def list_nodes(self):
        """List all nodes in the cluster"""
        print("Listing nodes:")
        nodes = self.core_v1.list_node()
        for node in nodes.items:
            print(f"Node: {node.metadata.name}")
    
    def list_pods(self, namespace="default"):
        """List all pods in a namespace"""
        print(f"Listing pods in namespace {namespace}:")
        pods = self.core_v1.list_namespaced_pod(namespace)
        for pod in pods.items:
            print(f"Pod: {pod.metadata.name} (Status: {pod.status.phase})")
    
    def list_deployments(self, namespace="default"):
        """List all deployments in a namespace"""
        print(f"Listing deployments in namespace {namespace}:")
        deployments = self.apps_v1.list_namespaced_deployment(namespace)
        for deploy in deployments.items:
            print(f"Deployment: {deploy.metadata.name} (Replicas: {deploy.status.replicas})")
    
    def create_namespace(self, name):
        """Create a new namespace"""
        namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=name))
        self.core_v1.create_namespace(namespace)
        print(f"Namespace {name} created")
    
    def delete_namespace(self, name):
        """Delete a namespace"""
        self.core_v1.delete_namespace(name)
        print(f"Namespace {name} deleted")

if __name__ == "__main__":
    handler = KubernetesHandlerReference()
    
    # Example usage
    handler.list_nodes()
    handler.list_pods()
    handler.list_deployments()
    
    # Uncomment to test namespace operations
    # handler.create_namespace("test-namespace")
    # handler.list_pods("test-namespace")
    # handler.delete_namespace("test-namespace")