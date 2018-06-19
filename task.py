# Load package
package = repository.read('Applications/k8s-Namespace-App/1.0')

# Load environment
environment = repository.read('Environments/gke')

# Start deployment
deploymentRef = deployment.prepareInitial(package.id, environment.id)
depl = deployment.prepareAutoDeployeds(deploymentRef)
task = deployment.createDeployTask(depl)
deployit.startTaskAndWait(task.id)
