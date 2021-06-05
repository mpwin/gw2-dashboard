import React from 'react';
import axios from 'axios';

import Collection from './Collection';
import CollectionList from './CollectionList';
import SkinList from './SkinList';
import WardrobeView from './WardrobeView';

class Wardrobe extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      collection:   null,
      weapon:       [],
      heavy_armor:  [],
      medium_armor: [],
      light_armor:  [],
      skins:        [],
      view:         'collection'
    };
  }

  selectCollection = (collection) => {
    this.setState({ collection: collection });
  }

  selectView = (view) => {
    this.setState({ view: view });
  }

  groupBy = (key, array) =>
    array.reduce((objectsByKeyValue, obj) => {
      const value = obj[key];
      objectsByKeyValue[value] = (objectsByKeyValue[value] || []).concat(obj);
      return objectsByKeyValue;
    }, {});

  componentDidMount() {
    axios.get('/api/collections.json')
      .then(res => {
        const collections = this.groupBy('category', res.data);
        const armor       = this.groupBy('weight_class', collections.Armor);

        this.setState({
          weapon:       collections.Weapon || [],
          heavy_armor:  armor.Heavy        || [],
          medium_armor: armor.Medium       || [],
          light_armor:  armor.Light        || []
        });
      });

    axios.get('/api/skins.json')
      .then(res => {
        this.setState({ skins: res.data });
      });
  }

  renderView = () => {
    switch (this.state.view) {
      case 'collection':
        return (
          <div className='container'>
            <div><CollectionList name='Weapon'       collections={this.state.weapon}       selectCollection={this.selectCollection} selectedCollection={this.state.collection} /></div>
            <div><CollectionList name='Heavy Armor'  collections={this.state.heavy_armor}  selectCollection={this.selectCollection} selectedCollection={this.state.collection} /></div>
            <div><CollectionList name='Medium Armor' collections={this.state.medium_armor} selectCollection={this.selectCollection} selectedCollection={this.state.collection} /></div>
            <div><CollectionList name='Light Armor'  collections={this.state.light_armor}  selectCollection={this.selectCollection} selectedCollection={this.state.collection} /></div>
          </div>
        );
        break;
      case 'standalone':
        return (
          <div className='container'>
            <div><SkinList skins={this.state.skins} /></div>
          </div>
        );
        break;
    }
  }

  render() {
    return (
      <div className='container'>
        <div><Collection collection={this.state.collection} /></div>
        {this.renderView()}
        <div><WardrobeView view={this.state.view} selectView={this.selectView} /></div>
      </div>
    );
  }
}

export default Wardrobe;
