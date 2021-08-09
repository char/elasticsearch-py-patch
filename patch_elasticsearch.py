def do_patch():
  import elasticsearch

  class TransportMethodContainer:
    def do_verify_elasticsearch_sync(self, *_a, **_k):
      self._verified_elasticsearch = True

    async def do_verify_elasticsearch_async(self, *_a, **_k):
      self._verified_elasticsearch = True

  sync_transport = elasticsearch.Transport
  sync_verifier = sync_transport._do_verify_elasticsearch
  sync_verifier.__code__ = TransportMethodContainer.do_verify_elasticsearch_sync.__code__

  async_transport = elasticsearch.AsyncTransport
  if async_transport is not None:  # If the 'async' extra is enabled
    async_verifier = async_transport._do_verify_elasticsearch
    async_verifier.__code__ = TransportMethodContainer.do_verify_elasticsearch_async.__code__
