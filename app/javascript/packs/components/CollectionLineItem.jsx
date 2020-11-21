import React from 'react';
import classNames from 'classnames';

class CollectionLineItem extends React.Component {
  handleClick = (collection) => {
    this.props.showCollection(collection);
  }

  render() {
    let liClass = classNames(
      'list-group-item',
      { 'list-group-item-success': this.props.collection.unlocked }
    );

    return(
      <li className={liClass} onClick={this.handleClick.bind(this, this.props.collection)}>
        {this.props.collection.name}
      </li>
    );
  }
}

export default CollectionLineItem;
