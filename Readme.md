# HTTP Server

To start the HTTP Server run command:
	"python3 httpserver.py <PortNumber>"

To run the test file run command:
	"python3 test.py <PortNumber>"
	
In order to stop the server use:
	"quit"

Images, videos, text files, etc all can be displayed in the browser.

## GET Method:

	Status 200 OK:
	GET request returns status 200 whenever a request is successful.

	Status 301 Moved Permanantly:
	GET request returns 301 when request to a file is redirected to a new location.
	
	Status 304 Not Modified:
	GET request returns status 304 when the requested file is not modified since it was last accessed.
	
	Status 403 Forbidden:
	GET request returns status 403 when the requested file exists but it doesn't have read permissions.
	
	Status 404 Not Found:
	GET request returns status 404 when the requested file doesn't exist.

	Status 414 URI Too Long:
	GET request returns status 414 when the requested uri is longer than the limit specified in config file.
	
	Status 415 Unsupported Media Type:
	GET request returns status 415 when the requested file has an extension of the file which is not supported by our server.
	
	Status 505 HTTP version not supported:
	GET request returns status 505 when the specified HTTP version in the request is other than HTTP/1.1 .

## POST Method:
	Status 200 OK:
	POST request retuens 200 when the request is successful.
	
	Status 404 Not Found:
	POST request returns status 404 when the requested file doesn't is not found at the server's end.
	
	Status 413 Payload Too Large:
	POST request returns 413 whenever the length of payload is larger than that specified in the config file.
	
	Status 505 HTTP version not supported:
	POST request returns status 505 when the specified HTTP version in the request is other than HTTP/1.1 .

## HEAD Method:
	Status 200 OK:
	HEAD request returns status 200 whenever a request is successful.
	
	Status 304 Not Modified:
	HEAD request returns status 304 when the requested file is not modified since it was last accessed.
	
	Status 404 Not Found:
	HEAD request returns status 404 when the requested file doesn't exist.
	
	Status 415 Unsupported Media Type:
	HEAD request returns status 415 when the requested file has an extension of the file which is not supported by our server.
	
	Status 505 HTTP version not supported:
	HEAD request returns status 505 when the specified HTTP version in the request is other than HTTP/1.1 .

## PUT Method:
	Status 200 OK:
	PUT request returns status 200 whenever a request is successful.
	
	Status 201 Created:
	PUT request returns status 201 when a new file is requested in order to complete this request.
	
	Status 204 No Content:
	PUT request returns status 204 when the requested file to be edited has 0 length of body.
	
	Status 304 Not Modified:
	PUT request returns status 304 when the requested file is not modified since it was last accessed.
	
	Status 403 Forbidden:
	PUT request returns status 403 when the requested file has no write permissions in order to edit it.
	
	Status 404 Not Found:
	PUT request returns status 404 when the requested file doesn't exist.
	
	Status 411 Length Required:
	PUT request returns status 411 when the request doesn't contain the "Content-Length Header".

	Status 413 Payload Too Large:
	PUT request returns 413 whenever the length of payload is larger than that specified in the config file.

	Status 414 URI Too Long:
	PUT request returns status 414 when the requested uri is longer than the limit specified in config file.
	
	Status 415 Unsupported Media Type:
	PUT request returns status 415 when the requested file has an extension of the file which is not supported by our server.
	
	Status 505 HTTP version not supported:
	PUT request returns status 505 when the specified HTTP version in the request is other than HTTP/1.1 .

## DELETE Method:
	Status 200 OK:
	DELETE request returns status 200 whenever a request is successful.
	
	Status 204 No Content:
	DELETE request returns status 204 when the requested file to be deleted has 0 length.
	
Apart from these some common status codes are:
	Status 400 Bad request:
	This status code is returned when the syntax of our request is not correct.
	
	Status 408 Request timed out:
	When the response is not generated within the specified time limit(specified in config file) the server returns status 408 as the 			request times out.
	
	Status 501 Method Not Impelemented:
	When client request requests method other than GET, POST, PUT, HEAD, DELETE then server returns 501 status code.
	


## Authors:
	Manish Arora
	Muskan Paryani
	
	
	
	
	
	
	
	
	
	
	
	
	
