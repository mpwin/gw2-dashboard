import React from 'react';
import CollectionLineItem from './CollectionLineItem';

class CollectionList extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    var collections = this.props.collections.map((collection) => {
      return (
        <CollectionLineItem collection={collection} showCollection={this.props.showCollection} />
      );
    });

    return(
      <ul class='list-group text-monospace'>
        <li class='list-group-item active'>{this.props.name}</li>
        {collections}
      </ul>
    );
  }
}

export default CollectionList;
