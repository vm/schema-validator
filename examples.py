from validate import validate

input_1 = {
    'assets': [
        {
            'ticker': 'AAPL',
            'price': 100.2,
            'is_equity': True, # bool
            'related_tickers': ['GOOG', 'MSFT'] # list of strings
        }
    ],
    'dates': ['2011/02/03', '2012/04/05']
}

schema1 = {
    'type': dict,
    'properties': {
        'assets': {
            'type': dict,
            'items': {
                'type': dict,
                'properties': {
                    'ticker': { 'type': str },
                    'price': { 'type': float },
                    'is_equity': { 'type': bool },
                    'related_tickers': {
                        'type': list,
                        'items': { 'type': str }
                    }
                },
                'additional_properties': {},
                'required': ['ticker', 'price', 'is_equity', 'related_tickers']
            }
        },
        'dates': {
            'type': list,
            'items': { 'type': str, 'format': 'date'}
        }
    },
    'additional_properties': {},
    'required': ['assets']
}

input_2 = {
    'conditions': {
      'AAPL': { 'type': 'between', 'min': 90, 'max': 95 },
      'MSFT': { 'type': 'greater than', 'min': 60 },
      'CSCO': { 'type': 'less than', 'max': 80 }
    }
}

schema2 = {
    'type': dict,
    'properties': {
        'conditions': {
            'type': dict,
            'properties': {},
            'additional_properties': {
                'type': dict,
                'properties': {
                    'type': { 'type': str },
                    'min': { 'type': int },
                    'max': { 'type': int }
                },
                'required': ['type'],
                'additional_properties': {}
            },
            'required': []
        }
    },
    'additional_properties': {},
    'required': ['conditions']
}

@validate(schema1)
def func_1(param):
    print input_1


@validate(schema2)
def func_2(param):
    print input_2

func_1(input_1)
func_2(input_2)
