
def handler(context, event):
    context.logger.info('This is function 1')

    return context.Response(body='Hello, from function 1',
                            headers={},
                            content_type='text/plain',
                            status_code=200)
