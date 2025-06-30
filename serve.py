from livereload import Server

server = Server()
server.watch('*.html')
server.watch('*.css')
server.watch('*.js')  # optional, if you have JS
server.serve(root='.')

