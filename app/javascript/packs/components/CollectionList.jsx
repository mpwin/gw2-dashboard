import React from 'react'
import classNames from 'classnames'

class CollectionList extends React.Component {
  constructor(props) {
    super(props);
  }

  handleClick = (collection) => {
    this.props.showCollection(collection);
  }

  render() {
    var collections = this.props.collections.map((collection) => {
      return (
        <li class={classNames('list-group-item', { 'list-group-item-success': collection.unlocked })} onClick={this.handleClick.bind(this, collection)}>
          {collection.name}
        </li>
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
