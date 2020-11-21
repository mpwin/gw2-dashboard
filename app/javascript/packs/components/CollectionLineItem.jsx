import React from 'react';
import classNames from 'classnames';

class CollectionLineItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hover: false };
  }

  getClass = () => {
    if (this.isSelected()) {
      return 'list-group-item-primary';
    }

    if (this.state.hover) {
      return this.props.collection.unlocked ? 'list-group-item-light' : 'list-group-item-dark';
    }

    if (this.props.collection.unlocked) {
      return 'list-group-item-success';
    }
  }

  handleClick = (collection) => {
    this.props.selectCollection(collection);
  }

  isSelected = () => {
    return this.props.collection == this.props.selectedCollection;
  }

  setHover = (hover) => {
    this.setState({ hover: hover });
  }

  render() {
    let liClass = classNames('list-group-item', this.getClass(), { 'cursor-pointer': !this.isSelected() });

    return(
      <li className={liClass} onClick={() => this.handleClick(this.props.collection)} onMouseEnter={() => this.setHover(true)} onMouseLeave={() => this.setHover(false)}>
        {this.props.collection.name}
      </li>
    );
  }
}

export default CollectionLineItem;
