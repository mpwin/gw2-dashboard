import React from 'react';
import CollectionLineItem from './CollectionLineItem';

class CollectionList extends React.Component {
  render() {
    var collections = this.props.collections.map((collection) => {
      return (
        <CollectionLineItem collection={collection} selectCollection={this.props.selectCollection} selectedCollection={this.props.selectedCollection} />
      );
    });

    return(
      <ul>
        <li className='active'>{this.props.name}</li>
        {collections}
      </ul>
    );
  }
}

export default CollectionList;
