
def handler(context, event):
    context.logger.info('This is function 3')

    return context.Response(body='Hello, from function 3',
                            headers={},
                            content_type='text/plain',
                            status_code=200)
