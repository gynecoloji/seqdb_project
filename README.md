# SeqDB - Sequencing Data Database

A professional database system for managing bulk RNA-seq and scRNA-seq data.

## Features

- **SQLite metadata tracking** - Track samples, datasets, experimental conditions
- **Parquet storage** - Efficient columnar storage with compression
- **DuckDB analytics** - Fast queries without loading full datasets
- **Snakemake pipelines** - Reproducible data processing
- **CLI interface** - Easy command-line access

## Installation
```bash
# Clone repository
git clone https://github.com/yourusername/seqdb.git
cd seqdb

# Install in development mode
pip install -e .
```

## Quick Start
```python
from seqdb.database import MetadataDB
from seqdb.converter import DataConverter

# Initialize database
db = MetadataDB('data/metadata.db')

# Convert data to Parquet
converter = DataConverter('data/parquet')
converter.bulk_to_parquet('data/raw/bulk/sample.csv', 'BULK001')
```

## Data Structure

- **Bulk RNA-seq**: Wide format (genes × samples)
- **scRNA-seq**: Sparse long format (non-zero values only)

## Project Structure
```
seqdb/
├── seqdb/          # Python package
├── data/           # Data storage (not in Git)
├── pipelines/      # Snakemake workflows
└── docs/           # Documentation
```

## License

MIT License