
def handler(context, event):
    context.logger.info('This is function 2')

    return context.Response(body='Hello, from function 2',
                            headers={},
                            content_type='text/plain',
                            status_code=200)
