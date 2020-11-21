import React from 'react';
import classNames from 'classnames';

class CollectionLineItem extends React.Component {
  handleClick = (collection) => {
    this.props.showCollection(collection);
  }

  render() {
    return(
      <li className={classNames('list-group-item', { 'list-group-item-success': this.props.collection.unlocked })} onClick={this.handleClick.bind(this, this.props.collection)}>
        {this.props.collection.name}
      </li>
    );
  }
}

export default CollectionLineItem;
