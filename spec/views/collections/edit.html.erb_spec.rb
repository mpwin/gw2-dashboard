require 'rails_helper'

RSpec.describe "collections/edit", type: :view do
  before(:each) do
    @collection = assign(:collection, Collection.create!(
      name: "MyString",
      unlocked: false,
      note: "MyText"
    ))
  end

  it "renders the edit collection form" do
    render

    assert_select "form[action=?][method=?]", collection_path(@collection), "post" do

      assert_select "input[name=?]", "collection[name]"

      assert_select "input[name=?]", "collection[unlocked]"

      assert_select "textarea[name=?]", "collection[note]"
    end
  end
end
