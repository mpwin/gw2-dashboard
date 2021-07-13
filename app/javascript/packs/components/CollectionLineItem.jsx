import React from 'react';
import classNames from 'classnames';

class CollectionLineItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hover: false };
  }

  getClass = () => {
    if (this.isSelected()) {
      return 'selected';
    }

    if (this.state.hover) {
      return this.props.collection.unlocked ? 'hover-unlocked' : 'hover-locked';
    }

    if (this.props.collection.unlocked) {
      return 'unlocked';
    }
  }

  isSelected = () => {
    return this.props.collection == this.props.selectedCollection;
  }

  setHover = (hover) => {
    this.setState({ hover: hover });
  }

  render() {
    let liClass = classNames(this.getClass(), { 'cursor-pointer': !this.isSelected() });

    return(
      <li className={liClass} onClick={() => this.props.selectCollection(this.props.collection)} onMouseEnter={() => this.setHover(true)} onMouseLeave={() => this.setHover(false)}>
        {this.props.collection.name}
      </li>
    );
  }
}

export default CollectionLineItem;
