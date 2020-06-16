require 'rails_helper'

RSpec.describe "skins/edit", type: :view do
  before(:each) do
    @skin = assign(:skin, Skin.create!(
      name: "MyString"
    ))
  end

  it "renders the edit skin form" do
    render

    assert_select "form[action=?][method=?]", skin_path(@skin), "post" do

      assert_select "input[name=?]", "skin[name]"
    end
  end
end
