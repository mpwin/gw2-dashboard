import React from 'react';
import classNames from 'classnames';

class CollectionLineItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hover: false };
  }

  handleClick = (collection) => {
    this.props.selectCollection(collection);
  }

  setHover = (hover) => {
    this.setState({ hover: hover });
  }

  render() {
    let selected = this.props.collection == this.props.selectedCollection;
    let liClass  = classNames(
      'list-group-item', { 'cursor-pointer': !selected },
      { 'list-group-item-primary': selected },
      { 'list-group-item-success': ( this.props.collection.unlocked && !this.state.hover && !selected) },
      { 'list-group-item-light':   ( this.props.collection.unlocked &&  this.state.hover && !selected) },
      { 'list-group-item-dark':    (!this.props.collection.unlocked &&  this.state.hover && !selected) }
    );

    return(
      <li className={liClass} onClick={() => this.handleClick(this.props.collection)} onMouseEnter={() => this.setHover(true)} onMouseLeave={() => this.setHover(false)}>
        {this.props.collection.name}
      </li>
    );
  }
}

export default CollectionLineItem;
