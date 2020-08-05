import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import Collections from './Collections'

class Dashboard extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      weapons:      [],
      heavy_armor:  [],
      medium_armor: [],
      light_armor:  []
    };
  }

  groupBy = (key, array) =>
    array.reduce((objectsByKeyValue, obj) => {
      const value = obj[key];
      objectsByKeyValue[value] = (objectsByKeyValue[value] || []).concat(obj);
      return objectsByKeyValue;
    }, {});
  
  componentDidMount() {
    axios.get('/collections.json')
      .then(res => {
        const collections = this.groupBy('category', res.data);
        const armor       = this.groupBy('weight_class', collections.Armor);

        this.setState({
          weapons:      collections.Weapon || [],
          heavy_armor:  armor.Heavy        || [],
          medium_armor: armor.Medium       || [],
          light_armor:  armor.Light        || []
        });
      });
  }

  render() {
    return (
      <div class='container-fluid'>
        <h1>Dashboard</h1>
        
        <Collections collections={this.state.weapons} />
        <Collections collections={this.state.heavy_armor} />
        <Collections collections={this.state.medium_armor} />
        <Collections collections={this.state.light_armor} />
      </div>
    );
  }
}

document.addEventListener('turbolinks:load', () => {
  const app = document.getElementById('dashboard')
  app && ReactDOM.render(<Dashboard />, app)
})
