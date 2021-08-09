# elasticsearch-py-patch

DRM patcher for the `elasticsearch-py` project.

See: https://github.com/elastic/elasticsearch-py/pull/1623

## Usage

```python
import patch_elasticsearch
import elasticsearch

if __name__ == "__main__":
  patch_elasticsearch.patch()
  # Connect to wherever you want
```
