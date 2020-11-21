import React from 'react';
import classNames from 'classnames';

class CollectionLineItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hover: false };
  }

  handleClick = (collection) => {
    this.props.showCollection(collection);
  }

  setHover = (hover) => {
    this.setState({ hover: hover });
  }

  render() {
    let liClass = classNames(
      'list-group-item', 'cursor-pointer',
      { 'list-group-item-success': ( this.props.collection.unlocked && !this.state.hover) },
      { 'list-group-item-light':   ( this.props.collection.unlocked &&  this.state.hover) },
      { 'list-group-item-dark':    (!this.props.collection.unlocked &&  this.state.hover) }
    );

    return(
      <li className={liClass} onClick={this.handleClick.bind(this, this.props.collection)} onMouseEnter={this.setHover.bind(this, true)} onMouseLeave={this.setHover.bind(this, false)}>
        {this.props.collection.name}
      </li>
    );
  }
}

export default CollectionLineItem;
