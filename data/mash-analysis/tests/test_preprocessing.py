def test_clean_data():
    # Test case for cleaning raw data
    raw_data = {
        'gene_id': ['gene1', 'gene2', 'gene3', None],
        'expression': [10, 20, None, 30]
    }
    cleaned_data = clean_data(raw_data)
    assert cleaned_data is not None
    assert len(cleaned_data) == 3  # Should remove the row with None values

def test_normalize_data():
    # Test case for normalizing data
    expression_data = {
        'gene1': [10, 20, 30],
        'gene2': [20, 30, 40]
    }
    normalized_data = normalize_data(expression_data)
    assert normalized_data is not None
    assert all(normalized_data['gene1'] <= 1)  # Normalized values should be <= 1
    assert all(normalized_data['gene2'] <= 1)

def test_transform_data():
    # Test case for transforming data
    expression_data = {
        'gene1': [10, 20, 30],
        'gene2': [20, 30, 40]
    }
    transformed_data = transform_data(expression_data)
    assert transformed_data is not None
    assert 'log2' in transformed_data.columns  # Check if log2 transformation is applied

# Add more tests as needed for other functions in preprocessing.py