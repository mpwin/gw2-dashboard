import React from 'react';
import { render } from '@testing-library/react';

import CollectionLineItem from './CollectionLineItem';

describe('CollectionLineItem', () => {
  test('renders', () => {
    const collection = {
      name: 'Collection Name',
      unlocked: true
    };

    render(<CollectionLineItem collection={collection} />);
  });
});
