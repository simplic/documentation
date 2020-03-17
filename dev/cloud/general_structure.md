## General structure

Simplic cloud solution is based on microservice architecture. However, there're some deviations from "shared nothing" microservice concept:
- all microservices share same technological stack and base libraries
- there's a shared database (however, each microservice owns a subset of collections)

A typical microservice solution:
- is created for a dedicated business context and named after it. For example, Logistics context is managed by Simplic.Cloud.Logistics microservice
- has following projects:
  - Simplic.Cloud.[BusinessContext].WebApi - .NET Core Web Api project, based on Simplic.Cloud.WebApi package. It serves read requests and sends write requests to worker service
  - Simplic.Cloud.[BusinessContext].Service - .NET Core console project, based on Simplic.Cloud.WorkerService package. It processes write requests, responds to WebApi and emits events, which others microservices can listen to
  - Simplic.Cloud.[BusinessContext] - .NET Core class library with shared code for WebApi and Service projects
  - Simplic.Cloud.[BusinessContext].Api.Model - .NET Core Standard library with classes for external clients
- uses MassTransit with RabbitMQ transport to communicate between WebApi and Service and with other microservices
- has configs for Azure Pipelines build, Kubernetes deployment and Ambassador mapping