# Authentication SDK with Django

This is an authentication SDK in Django convens the following futures:
1. Authenticate users against multiple servers and get permission parameters without code duplication.
2. Centralize all the logic connecting to the authentication service.
3. Cache permission across services
4. Avoid code duplication in models.
5. Avoid breaking changes in the database structure.

<p align="center">
  <img src="https://miro.medium.com/max/581/1*MSgbloMVqwP8bsQvzEub1A.png" width="400" alt="Authentication SKD in Django">
</p>

In the above diagram, a user requests a JWT directly from the authentication service, this JWT will be used to authenticate against every future service. The SDK authenticates the user based on the JWT and, in turn, requests permission parameters from the authentication service within the network using http requests between servers.

## SDK
The developer should be able to run `pip install auth-sdk` that will create a now microservice with the ability to communicate between services and with the client. 

The SDK is really just a django app with three important files: models.py, dbrouter.py and authentication.py.
