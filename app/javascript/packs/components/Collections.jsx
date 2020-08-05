import React from 'react'
import classNames from 'classnames'

class Collections extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    var collections = this.props.collections.map((collection) => {
      return (
        <li class={classNames('list-group-item', { 'list-group-item-success': collection.unlocked })}>
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

export default Collections;
